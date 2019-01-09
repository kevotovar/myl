$(document).ready(function () {
  var table = $('#datatable').DataTable({
    language: {
      sProcessing: "Procesando...",
      sLengthMenu: "Mostrar _MENU_ registros",
      sZeroRecords: "No se encontraron resultados",
      sEmptyTable: "Ningún dato disponible en esta tabla",
      sInfo: "Mostrando registros del _START_ al _END_ de un total de _TOTAL_ registros",
      sInfoEmpty: "Mostrando registros del 0 al 0 de un total de 0 registros",
      sInfoFiltered: "(filtrado de un total de _MAX_ registros)",
      sInfoPostFix: "",
      sSearch: "Buscar:",
      sUrl: "",
      sInfoThousands: ",",
      sLoadingRecords: "Cargando...",
      paginate: {
        next: ">",
        previous: "<",
        first: "<<",
        last: ">>"
      },
      oAria: {
      sSortAscending: ": Activar para ordenar la columna de manera ascendente",
      sSortDescending: ": Activar para ordenar la columna de manera descendente"
      }
    },
    order: [[1, 'desc']],
    columnDefs: [
      {
        name: 'ranking_id',
        orderable: false,
        searchable: true,
        targets: [0]
      },
      {
        name: 'name',
        orderable: true,
        searchable: true,
        targets: [1]
      },
      {
        name: 'points',
        orderable: true,
        searchable: true,
        targets: [2]
      }
    ],
    searching: true,
    processing: true,
    serverSide: true,
    ajax: $('#datatable-url').val()
  });
});
