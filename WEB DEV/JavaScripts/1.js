var product = 2.0 * 2.5; 

promise = new Promise(function (resolve, reject) {
	resolve(4)
        }).then(
            function (result) { 
                return result*3;
             }
        ).then(
        	function (result) { 
                alert(result);
             }
        );
