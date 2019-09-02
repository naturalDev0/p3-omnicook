// Global variables
var nextNo;

$(document).ready(function() {
    
    nextNo = 1;
    $('.add-row').click(function(e) {
        e.preventDefault();
        addRowId = 'field' + nextNo;
        addRow = '#field' + nextNo;

        var newRow = '<div class="form-row justify-content-center" id="' + addRowId + '">' +
            '<div class="form-group col-md-5">' +
            '<input type="text" class="form-control" name="ingred-name[]" id="ingred-name-[]" placeholder="insert your ingredient...">' +
            '</div>' +
            '<div class="form-group col-md-5">' +
            '<input type="text" class="form-control" name="ingred-serve[]" id="ingred-serve-[]" placeholder="insert your ingredient serving...">' +
            '</div>' +
            '<div class="form-group col-md-1 text-center">' +
            '<button type="text" class="btn btn-danger align-middle remove-row" role="button" value=' + addRow + '>Remove</button>' +
            '</div>' +
            '</div>'

        $('#fields').append(newRow);
        nextNo = nextNo + 1;

    });
    
    $('#fields').on('click', '.remove-row', function(e) {
        e.preventDefault();
        var btnVal = $(this).val();
        console.log(btnVal);
        $(btnVal).remove();
    });
    
});
