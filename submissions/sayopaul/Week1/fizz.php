<?php

	for($i=1; $i<=100; $i++){

		$output =  ($i % 15 === 0) ? "FizzBuzz".PHP_EOL  :  ( ($i % 3 === 0)  ? "Fizz".PHP_EOL :  ( ($i % 5 === 0 ) ? "Buzz".PHP_EOL : $i.PHP_EOL ));

		/*
			original version(longer)
		if($i % 15 === 0 ){

			$output = "FizzBuzz".PHP_EOL;	

			

			
		}elseif($i % 3 === 0 ){

			$output = "Fizz".PHP_EOL;

		}elseif($i % 5 === 0 ){

			$output = "Buzz".PHP_EOL;

		}else{
			$output = $i.PHP_EOL;
		}*/
		echo $output;
	}



	