var defaultData = {
  participants: 4,
  places: {},
  disableSubmit: true
};

var tournamentReportUrl = $('#tournament-report-url').val();

var app = new Vue({
  el: '#app',
  data: Object.assign({}, defaultData),
  computed: {
    participantsRows: function () {
      var acc = [];
      for(var i=1; i <= this.participants; i++) {
        acc.push(i);
      }
      return acc;
    }
  },
  watch: {
    places: function () {
      this.checkSubmitEnabled();
    }
  },
  methods: {
    sendTournamentReport: function () {
      var csrfmiddlewaretoken = $('input[name="csrfmiddlewaretoken"]').val();
      $.post(tournamentReportUrl, Object.assign({
          csrfmiddlewaretoken: csrfmiddlewaretoken,
        }, this.places))
        .always(function () {
          swal('Mandando reporte');
          swal.showLoading();
        })
        .done(function(response) {
          swal(response.success, 'En 5 segundos se refrescara esta pantalla...');
        })
        .fail(function (response) {
          swal({
            type: 'error',
            title: 'Ocurrio un error',
          });
        })
    },
    reset: function () {
      this.participants = defaultData.participants;
      this.places = {};
    },
    checkSubmitEnabled: function () {
      var placesKeys = Object.keys(this.places);
      var self = this;
      if (!placesKeys.size) {
        self.disableSubmit = true;
      }
      var invalidKeys = [];
      for (var i = 1; i <= self.participants; i++) {
        console.log('self.places['+i+']', self.places[i]);
        self.places[i] || invalidKeys.push(self.places[i]);
      }
      self.disableSubmit = Boolean(invalidKeys.length);
    }
  }
});
