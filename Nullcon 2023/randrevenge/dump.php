<?php

$fp = fopen('data2.csv', 'a')or die("Unable to open file!");

$lines = "";
for($i=0;$i<20796091;$i++){
    mt_srand($i);

    if ($i % 1000000 == 0) {
        // percent complete
        fwrite(STDERR, ($i / 20796091) * 100 . "%\n");
        fwrite($fp, $lines);
        $lines = "";
    }

    $x1 = mt_rand();

    $lines .= "$x1,$i\n";
}