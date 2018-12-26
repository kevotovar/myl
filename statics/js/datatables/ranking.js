$(document).ready(function () {
  var dataTable = $('#datatable').dataTable({
    order: [[2, 'desc']],
    columnDefs: [
      {
        name: 'ranking_id',
        orderable: true,
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
