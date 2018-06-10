<?php

	for($i=1; $i<=100; $i++){

		if($i % 15 === 0 ){
			$output = "FizzBuzz".PHP_EOL;	

		}elseif($i % 3 === 0 ){
			$output = "Fizz".PHP_EOL;

		}elseif($i % 5 === 0 ){
			$output = "Buzz".PHP_EOL;

		}else{
		    $output = $i.PHP_EOL;
		}
		echo $output;

	}