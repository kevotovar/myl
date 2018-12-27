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
    order: [[2, 'desc']],
    columnDefs: [
      {
        searchable: false,
        orderable: false,
        targets: 0
      },
      {
        name: 'ranking_id',
        orderable: false,
        searchable: true,
        targets: [1]
      },
      {
        name: 'name',
        orderable: true,
        searchable: true,
        targets: [2]
      },
      {
        name: 'points',
        orderable: true,
        searchable: true,
        targets: [3]
      }
    ],
    searching: true,
    processing: true,
    serverSide: true,
    ajax: $('#datatable-url').val()
  });
  table.on( 'order.dt search.dt', function () {
      table.column(0, {search:'applied', order:'applied'}).nodes().each( function (cell, i) {
      cell.innerHTML = i+1;
    });
  }).draw();
});
