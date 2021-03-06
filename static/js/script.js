// Global variables
var nextNo;
var getLastChildFlag

$(document).ready(function() {
    
    nextNo = 1;
    getLastChildFlag = false;
    $('.add-row').click(function(e) {
        e.preventDefault();
        
        var tempIdNo = $('#fields').children().last().attr('id');
        console.log(tempIdNo, getLastChildFlag)
        if ((tempIdNo != undefined) && (getLastChildFlag == false)) {
            var get_tempIdNo = parseInt(tempIdNo.replace('field',''));
            nextNo = get_tempIdNo + 1;
            getLastChildFlag = true;
        }
        console.log("What is get_tempIdNo now?: " + get_tempIdNo);
        
        addRowId = 'field' + nextNo;
        addRow = '#field' + nextNo;
        
        console.log(addRowId, addRow);
        
        var newRow = '<div class="form-row justify-content-center" id="' + addRowId + '">' +
            '<div class="form-group col-md-5">' +
            '<input type="text" class="form-control" name="ingred-name[]" id="ingred-name-[]" placeholder="insert your ingredient...">' +
            '</div>' +
            '<div class="form-group col-md-5">' +
            '<input type="text" class="form-control" name="ingred-serve[]" id="ingred-serve-[]" placeholder="insert your ingredient serving...">' +
            '</div>' +
            '<div class="form-group col-md-1 text-center">' +
            '<button type="text" class="btn btn-danger align-middle remove-row" role="button" value=' + addRow + '><svg id="i-minus" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32" width="1rem" height="1rem" fill="none" stroke="currentcolor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"><path d="M2 16 L30 16" /></svg><span class="align-baseline"> Remove<span></button>' +
            '</div>' +
            '</div>'

        $('#fields').append(newRow);
        nextNo = nextNo + 1;
        

    });
    
    $('#fields').on('click', '.remove-row', function(e) {
        e.preventDefault();
        var btnVal = $(this).val();
        console.log('Removed button: ' + btnVal);
        $(btnVal).remove();
    });
    
});
