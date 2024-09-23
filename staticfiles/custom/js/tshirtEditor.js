var canvas;
var tshirts = []; // Prototype: [{style:'x', color:'white', front:'a', back:'b', price:{tshirt:'12.95', frontPrint:'4.99', backPrint:'4.99', total:'22.47'}}]
var a;
var b;
var line1;
var line2;
var line3;
var line4;


$(document).ready(function () {

    document.getElementById('add-text').onclick = function () {
        var text = $("#text-string").val();
        var textSample = new fabric.Text(text, {
            left: fabric.util.getRandomInt(0, 200),
            top: fabric.util.getRandomInt(0, 400),
            fontFamily: 'helvetica',
            angle: 0,
            fill: '#000000',
            scaleX: 0.5,
            scaleY: 0.5,
            fontWeight: '',
            hasRotatingPoint: true
        });
        canvas.add(textSample);
        textSample.set({ hasRotatingPoint: true });
        $("#texteditor").css('display', 'block');
        $("#imageeditor").css('display', 'block');
    };

    $("#text-string").keyup(function () {
        var activeObject = canvas.getActiveObject();
        if (activeObject && activeObject.type === 'text') {
            activeObject.set('text', this.value);
            canvas.renderAll();
        }
    });

    $(".img-polaroid").click(function (e) {
        var el = e.target;
        var offset = 50;
        var left = fabric.util.getRandomInt(0 + offset, 200 - offset);
        var top = fabric.util.getRandomInt(0 + offset, 400 - offset);
        var angle = fabric.util.getRandomInt(-20, 40);
        var width = fabric.util.getRandomInt(30, 50);
        var opacity = Math.random() * (1 - 0.5) + 0.5;

        fabric.Image.fromURL(el.src, function (image) {
            image.set({
                left: left,
                top: top,
                angle: 0,
                padding: 10,
                cornerSize: 10,
                hasRotatingPoint: true
            });
            canvas.add(image);
        });
    });



    document.getElementById('remove-selected').onclick = function () {
        var activeObject = canvas.getActiveObject();
        var activeObjects = canvas.getActiveObjects();
        if (activeObject) {
            canvas.remove(activeObject);
            $("#text-string").val("");
			var fileInput = document.getElementById('ownlogo');
			fileInput.value = '';
        } else if (activeObjects.length) {
            canvas.discardActiveObject();
            activeObjects.forEach(function (object) {
                canvas.remove(object);
            });
        }
    };

    document.getElementById('bring-to-front').onclick = function () {
        var activeObject = canvas.getActiveObject();
        var activeObjects = canvas.getActiveObjects();
        if (activeObject) {
            activeObject.bringToFront();
        } else if (activeObjects.length) {
            activeObjects.forEach(function (object) {
                object.bringToFront();
            });
        }
    };

    document.getElementById('send-to-back').onclick = function () {
        var activeObject = canvas.getActiveObject();
        var activeObjects = canvas.getActiveObjects();
        if (activeObject) {
            activeObject.sendToBack();
        } else if (activeObjects.length) {
            activeObjects.forEach(function (object) {
                object.sendToBack();
            });
        }
    };

    $("#text-bold").click(function () {
        var activeObject = canvas.getActiveObject();
        if (activeObject && activeObject.type === 'text') {
            activeObject.set('fontWeight', activeObject.fontWeight === 'bold' ? '' : 'bold');
            canvas.renderAll();
        }
    });

    $("#text-italic").click(function () {
        var activeObject = canvas.getActiveObject();
        if (activeObject && activeObject.type === 'text') {
            activeObject.set('fontStyle', activeObject.fontStyle === 'italic' ? '' : 'italic');
            canvas.renderAll();
        }
    });

	$("#text-strike").click(function () {
		var activeObject = canvas.getActiveObject();
		if (activeObject && activeObject.type === 'text') {
			var currentDecoration = activeObject.get('textDecoration') || '';
			var newDecoration = currentDecoration.includes('line-through') ?
				currentDecoration.replace('line-through', '').trim() :
				currentDecoration + ' line-through';
			activeObject.set('textDecoration', newDecoration);
			canvas.requestRenderAll();
		}
	});

	$("#text-underline").click(function () {
		var activeObject = canvas.getActiveObject();
		if (activeObject && activeObject.type === 'text') {
			var currentDecoration = activeObject.get('textDecoration') || '';
			var newDecoration = currentDecoration.includes('underline') ?
				currentDecoration.replace('underline', '').trim() :
				currentDecoration + ' underline';
			activeObject.set('textDecoration', newDecoration);
			canvas.requestRenderAll();
		}
	});



    $("#text-left").click(function () {
        var activeObject = canvas.getActiveObject();
        if (activeObject && activeObject.type === 'text') {
            activeObject.set('textAlign', 'left');
            canvas.renderAll();
        }
    });

    $("#text-center").click(function () {
        var activeObject = canvas.getActiveObject();
        if (activeObject && activeObject.type === 'text') {
            activeObject.set('textAlign', 'center');
            canvas.renderAll();
        }
    });

    $("#text-right").click(function () {
        var activeObject = canvas.getActiveObject();
        if (activeObject && activeObject.type === 'text') {
            activeObject.set('textAlign', 'right');
            canvas.renderAll();
        }
    });

    $("#font-family").change(function () {
        var activeObject = canvas.getActiveObject();
        if (activeObject && activeObject.type === 'text') {
            activeObject.set('fontFamily', this.value);
            canvas.renderAll();
        }
    });

    $('#text-bgcolor').on('change', function () {
        var activeObject = canvas.getActiveObject();
        if (activeObject && activeObject.type === 'text') {
            activeObject.set('backgroundColor', this.value);
            canvas.renderAll();
        }
    });

    $('#text-fontcolor').on('change', function () {
        var activeObject = canvas.getActiveObject();
        if (activeObject && activeObject.type === 'text') {
            activeObject.set('fill', this.value);
            canvas.renderAll();
        }
    });

    $('#text-strokecolor').on('change', function () {
        var activeObject = canvas.getActiveObject();
        if (activeObject && activeObject.type === 'text') {
            activeObject.set('stroke', this.value);
            canvas.renderAll();
        }
    });

    $("#drawingArea").hover(
        function () {
            // canvas.add(line1);
            // canvas.add(line2);
            // canvas.add(line3);
            // canvas.add(line4);
            canvas.renderAll();
        },
        function () {
            canvas.remove(line1);
            canvas.remove(line2);
            canvas.remove(line3);
            canvas.remove(line4);
            canvas.renderAll();
        }
    );

    // $('.color-preview').click(function () {
    //     var color = $(this).css("background-color");
    //     document.getElementById("shirtDiv").style.backgroundColor = color;
    // });




    $(".clearfix button, a").tooltip();

    line1 = new fabric.Line([0, 0, 200, 0], { "stroke": "#000000", "strokeWidth": 1, hasBorders: false, hasControls: false, hasRotatingPoint: false, selectable: false });
    line2 = new fabric.Line([199, 0, 200, 399], { "stroke": "#000000", "strokeWidth": 1, hasBorders: false, hasControls: false, hasRotatingPoint: false, selectable: false });
    line3 = new fabric.Line([0, 0, 0, 400], { "stroke": "#000000", "strokeWidth": 1, hasBorders: false, hasControls: false, hasRotatingPoint: false, selectable: false });
    line4 = new fabric.Line([0, 400, 200, 399], { "stroke": "#000000", "strokeWidth": 1, hasBorders: false, hasControls: false, hasRotatingPoint: false, selectable: false });
}); // doc ready

function getRandomNum(min, max) {
    return Math.random() * (max - min) + min;
}

function onObjectSelected(e) {
    var selectedObject = e.target;
    $("#text-string").val("");
    selectedObject.set({ hasRotatingPoint: true });
    if (selectedObject && selectedObject.type === 'text') {
        // Display text editor
        $("#texteditor").css('display', 'block');
        $("#text-string").val(selectedObject.text);
        $('#text-fontcolor').val(selectedObject.fill);
        $('#text-strokecolor').val(selectedObject.stroke);
        $("#imageeditor").css('display', 'block');
    } else if (selectedObject && selectedObject.type === 'image') {
        // Display image editor
        $("#texteditor").css('display', 'block');
        $("#imageeditor").css('display', 'block');
    }
}

function onSelectedCleared(e) {
    $("#texteditor").css('display', 'block');
    $("#text-string").val("");
    $("#imageeditor").css('display', 'block');
}

function setFont(font) {
    var activeObject = canvas.getActiveObject();
    if (activeObject && activeObject.type === 'text') {
        activeObject.set('fontFamily', font);
        canvas.renderAll();
    }
}

function removeWhite() {
    var activeObject = canvas.getActiveObject();
    if (activeObject && activeObject.type === 'image') {
        activeObject.filters.push(new fabric.Image.filters.RemoveColor({
            color: '#FFFFFF',
            distance: 0.1
        }));
        activeObject.applyFilters();
        canvas.renderAll();
    }
}


// =========================

