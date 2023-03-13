<?php

$number_of_candidates = $argv[1];

$candidates = array();

for ($i = 0; $i < $number_of_candidates; $i++) {
    $candidates[] = intval($argv[$i + 2]);
}


$t = intval($argv[$number_of_candidates + 2]);
$x = intval($argv[$number_of_candidates + 3]);
$hints = array();

// request 5 hints
for ($i = 0; $i < 5; $i++) {
    $hints[] = intval($argv[$number_of_candidates + 4 + $i]);
}

//iterate over candidates
foreach ($candidates as $candidate) {
    mt_srand($candidate);
    mt_rand();
    $current_hint = 0;
    for ($i = 0; $i < 300; $i++) {
        if (($i % 60) == ($t % 60)) {
            $next = mt_rand();
            if ($current_hint < 6 && $next == $hints[$current_hint]) {
                $current_hint++;
            } else {
                continue 2;
            }
        } else {
            mt_rand();
        }
    }
    $next = mt_rand();
    echo "$next";
}