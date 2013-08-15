$(function () {

// Select/DeselectAll
	$("#toggle").on( "click", function (e) {
		e.preventDefault();
		var i = 0;
		$("#box3FoodsILikeList input").each( function() { 
			if ($(this).prop("checked") == 1){
				i++;
			}
		});
		if (i != 0){	
			$("#box3FoodsILikeList input").each( function() { 
				$(this).prop("checked", 0); 
			});
		}	
		else{
			$("#box3FoodsILikeList input").each( function() { 
				$(this).prop("checked", 1); 
			});
		}
	});

// Check all Foods in Foods I like
	$("#box3FoodsILikeList input").each( function() { 
		$(this).prop("checked", 1);
	});


//Change Metric/US system
	$("input[name=unitSystem]").change(function(){
        if ($('input[name=unitSystem]').filter(':checked').val() == "Metric"){
        	$('#MetricUnit').show();
        	$('#USUnit').hide();
        	$('#MetricUnitH').show();
        	$('#USUnitH').hide();
        	$('#USUnitHI').hide();

			}
       else if ($('input[name=unitSystem]').filter(':checked').val() == "US"){
			$('#USUnit').show();
			$('#MetricUnit').hide();
        	$('#MetricUnitH').hide();
        	$('#USUnitH').show();
        	$('#USUnitHI').show();
			}
	});


//Change nutrient plan on change
	$("input[name=nutrientPlan]").change(function(){
        if ($('input[name=nutrientPlan]').filter(':checked').val() == 1){
        	$("input[name^='Full']").parent().parent().hide();
			}
       else if ($('input[name=nutrientPlan]').filter(':checked').val() == 0){
			$("input[name^='Full']").parent().parent().show();
			}
	});


	
//Make nutrient plan first remain as basic
	if ($('input[name=nutrientPlan]').filter(':checked').val() == 1){
		$("input[name^='Full']").parent().parent().hide();
		}
   else if ($('input[name=nutrientPlan]').filter(':checked').val() == 0){
		$("input[name^='Full']").parent().parent().show();
		}

//Make nutrient plan first remain as basic
	if ($('input[id=nutrientPlan-0]').prop('checked') == 0){
		if ($('input[id=nutrientPlan-1]').prop('checked') == 0){
			$('input[id=nutrientPlan-0]').prop('checked', true);
			$("input[name^='Full']").parent().parent().hide();
			}
		}
   

	
//If the nutrients are selected but use other plans - make them unchecked
	$("input[name=opt_nut]").change(function(){
        if ($('input[name=opt_maxormin]').filter(':checked').val() >= 2){
			$("#listobj input").each( function() { 
				$(this).attr('checked', false); 
			});
		}	
	});

//If other plans are selected - cancel what is in the list object
	$("input[name=opt_maxormin]").change(function(){
        if ($('input[name=opt_maxormin]').filter(':checked').val() >= 2){
			$("#listobj input").each( function() { 
				$(this).attr('checked', false); 
			});
		}	
	});

//
	$("#box2ResultList li a").each(function(){
		$(this).mouseover(function(){
			var toShow = '#tabNut'+ $(this).attr('id');
			$("table[id^='tabNut']").hide();
			$(toShow).show();
		});
	});

});