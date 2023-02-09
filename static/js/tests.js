var system_currency=$('#system_currency').val();
var count=$('#count').val();

(function($){

    "use strict";

    //active
    $('#tests').addClass('active');

    //tests datatable
    var table=$('#tests_table').DataTable( {
      dom: "<'row'<'col-sm-4'l><'col-sm-4'B><'col-sm-4'f>>" +
      "<'row'<'col-sm-12'tr>>" +
      "<'row'<'col-sm-4'i><'col-sm-8'p>>",
      buttons: [
        {
            extend:    'copyHtml5',
            text:      '<i class="fas fa-copy"></i> '+trans("Copy"),
            titleAttr: 'Copy'
        },
        {
            extend:    'excelHtml5',
            text:      '<i class="fas fa-file-excel"></i> '+trans("Excel"),
            titleAttr: 'Excel'
        },
        {
            extend:    'csvHtml5',
            text:      '<i class="fas fa-file-csv"></i> '+trans("CVS"),
            titleAttr: 'CSV'
        },
        {
            extend:    'pdfHtml5',
            text:      '<i class="fas fa-file-pdf"></i> '+trans("PDF"),
            titleAttr: 'PDF'
        },
        {
          extend:    'colvis',
          text:      '<i class="fas fa-eye"></i>',
          titleAttr: 'colvis'
        }
        
      ],
      "processing": true,
      "serverSide": true,
      "bSort" : false,
        "ajax": {
          url: url("admin/get_tests")
        },
        // orderCellsTop: true,
        fixedHeader: true,
        "columns": [
           {data:"id"},
           {data:"name"},
           {data:"shortcut"},
           {data:"price"},
           {data:"action",searchable:false,orderable:false,sortable:false}//action
        ],
        "language": {
          "sEmptyTable":     trans("No data available in table"),
          "sInfo":           trans("Showing")+" _START_ "+trans("to")+" _END_ "+trans("of")+" _TOTAL_ "+trans("records"),
          "sInfoEmpty":      trans("Showing")+" 0 "+trans("to")+" 0 "+trans("of")+" 0 "+trans("records"),
          "sInfoFiltered":   "("+trans("filtered")+" "+trans("from")+" _MAX_ "+trans("total")+" "+trans("records")+")",
          "sInfoPostFix":    "",
          "sInfoThousands":  ",",
          "sLengthMenu":     trans("Show")+" _MENU_ "+trans("records"),
          "sLoadingRecords": trans("Loading..."),
          "sProcessing":     trans("Processing..."),
          "sSearch":         trans("Search")+":",
          "sZeroRecords":    trans("No matching records found"),
          "oPaginate": {
              "sFirst":    trans("First"),
              "sLast":     trans("Last"),
              "sNext":     trans("Next"),
              "sPrevious": trans("Previous")
          },
        }
     });
    
    // text editor
    $('.components').find('textarea').summernote({
      tabsize: 4,
      heigt:100,
      tooltip: false,
      dialogsFade: true,
      toolbar: [
        ['style', ['bold', 'italic', 'underline', 'clear']],
        ['fontsize', ['fontsize']],
        ['color', ['color']],
        ['para', ['ul', 'ol', 'paragraph']],
      ]
    });

    //components

    $('.add_component').on('click',function(){
            count++;
            $('.components .items').append(`
            <tr id="component_`+count+`" num="`+count+`">
               <td>
                    <div class="form-group">
                        <input type="text" class="form-control" name="component[`+count+`][name]" placeholder="`+trans('Component')+`" required>
                    </div>
               </td>
               <td>
                    <div class="form-group">
                        <textarea  class="form-control" name="component[`+count+`][result_template]" placeholder="`+trans('Result template')+`" required></textarea>
                    </div>
               </td>
               <td>
                    <button type="button" class="btn btn-danger delete_row">
                        <i class="fa fa-trash"></i>
                    </button>
               </td>
            </tr>
            `);
            //initialize text editor
            $('#component_'+count).find('textarea').summernote({
                tabsize: 4,
                heigt:100,
                tooltip: false,
                dialogsFade: true,
                toolbar: [
                  ['style', ['bold', 'italic', 'underline', 'clear']],
                  ['fontsize', ['fontsize']],
                  ['color', ['color']],
                  ['para', ['ul', 'ol', 'paragraph']],
                ]
            });
    });


    //delete test component
    $(document).on('click','.delete_row',function(){
        var test_id=$(this).closest('tr').attr('test_id');
        var el=$(this);

        swal({
          title: trans("Are you sure to delete component ?"),
          type: "warning",
          showCancelButton: true,
          confirmButtonClass: "btn-danger",
          confirmButtonText: trans("Delete"),
          cancelButtonText: trans("Cancel"),
          closeOnConfirm: true
        },
        function(){
          if(test_id!==undefined)
          {
            $.ajax({
              url:ajax_url('delete_test/'+test_id),
              beforeSend:function()
              {
                 $('.preloader').show();
                 $('.loader').show();
              },
              success:function()
              {
                $(el).parent().parent().remove();
              },
              complete:function(){
                $('.preloader').hide();
                $('.loader').hide();
              }
            });
          }
          else{
            $(el).parent().parent().remove();
          }
          
        });

    });

    //check if selected components
    $('#test_form').on('submit',function(){
      var count_components=$('.components tbody tr').length;

      if(count_components==0)
      {
        toastr.error(trans('Please select at least one test component'),trans('Failed'));
        return false;
      }

    });

    //delete test
    $(document).on('click','.delete_test',function(e){
        e.preventDefault();
        var el=$(this);
        swal({
          title: trans("Are you sure to delete test ?"),
          type: "warning",
          showCancelButton: true,
          confirmButtonClass: "btn-danger",
          confirmButtonText: trans("Delete"),
          cancelButtonText: trans("Cancel"),
          closeOnConfirm: false
        },
        function(){
          $(el).parent().submit();
        });
    });

})(jQuery);

