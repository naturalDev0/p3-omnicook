// Global variables
var nextNo;

// Load script's actions
$(document).ready(function() {

    nextNo = 2;
    $('.add-more').click(function(e) {
        e.preventDefault();
        addRow = '#field' + nextNo;
        addRemoveRow = '#field' + nextNo;
        nextNo = nextNo + 1;
        
        var newInput = '<div class="form-row" id="field' + nextNo + '">' + 
                        '<div class="form-group col-md-1"><span class="align-middle">'+ nextNo + '</span></div>' +
                        '<div class="form-group col-md-5"><input type="text" class="form-control" id="ingred-name-' + nextNo + '" placeholder="insert your ingredient..."></div>' +
                        '<div class="form-group col-md-5"><input type="text" class="form-control" id="ingred-serve-' + nextNo + '" placeholder="insert your ingredient serving..."></div>'
                        '<div class="form-group col-md-1 text-center"><div id="field">' +
                        '<button type="text" class="btn btn-primary align-middle add-more" role="button" id="field-btn1">Add</button></div></div>' +
                    '</div>';
        
        $('.remove-me').click(function(e) {
            e.preventDefault();
        //     var fieldNum = this.id.charAt(this.id.length - 1);
        //     var fieldID = "#field" + fieldNum;
        //     $(this).remove();
        //     $(fieldID).remove();
        });
    });

/*
    var next = 2;
    $(".add-more").click(function(e) {
        e.preventDefault();
        var addto = "#field" + next;
        var addRemove = "#field" + (next);
        next = next + 1;
        
        // Insert new row field on UI
        // var newIn = '<input autocomplete="off" class="input form-control" id="field' + next + '" name="field' + next + '" type="text">';
        var newIn = '<div class="form-row" id="field' + next + '">' + 
                        '<div class="form-group col-md-1"><span class="align-middle">'+ next + '</span></div>' +
                        '<div class="form-group col-md-5"><input type="text" class="form-control" id="ingred-name-' + next + '" placeholder="insert your ingredient..."></div>' +
                        '<div class="form-group col-md-5"><input type="text" class="form-control" id="ingred-serve-' + next + '" placeholder="insert your ingredient serving..."></div>'
                        '<div class="form-group col-md-1 text-center"><div id="field">' +
                        '<button type="text" class="btn btn-primary align-middle add-more" role="button" id="field1">Add</button></div></div>' +
                    '</div>';
        var newInput = $(newIn);
        
        // Remove row field on UI
        //var removeBtn = '<button id="remove' + (next - 1) + '" class="btn btn-danger remove-me" >Remove</button></div><div id="field">';
        var removeBtn = '<button type="text" id="remove' + (next-1) + '" class="btn btn-danger align-middle remove-me" role="button">Remove</button>'; 
        var removeButton = $(removeBtn);
        
        $("#fields").append(newInput);
        // $(addto).after(newInput);
        $(addRemove).after(removeButton);
        // $("#field" + next).attr('data-source', $(addto).attr('data-source'));
        // $("#count").val(next);

        $('.remove-me').click(function(e) {
            e.preventDefault();
            var fieldNum = this.id.charAt(this.id.length - 1);
            var fieldID = "#field" + fieldNum;
            $(this).remove();
            $(fieldID).remove();
        });
    });
*/
});
