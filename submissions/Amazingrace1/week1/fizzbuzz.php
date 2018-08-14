<?php

for ($i = 1; $i <= 100 ; $i++) { 
	$isFizz = (0 === $i % 3);
	$isBuzz = (0 === $i % 5);

	if (!$isFizz && !$isBuzz) {
		echo $i . PHP_EOL;
		continue;
	}
	if ($isFizz) {
		echo 'Fizz';
	}
	if ($isBuzz) {
		echo 'Buzz';
	}
	echo PHP_EOL;
}

?>