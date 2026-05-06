set ns [new Simulator]

set nf [open bus.nam w]
$ns namtrace-all $nf

set n0 [$ns node]
set n1 [$ns node]
set n2 [$ns node]
set n3 [$ns node]

$ns duplex-link $n0 $n1 1Mb 10ms DropTail
$ns duplex-link $n1 $n2 1Mb 10ms DropTail
$ns duplex-link $n2 $n3 1Mb 10ms DropTail

set udp [new Agent/UDP]
$ns attach-agent $n0 $udp

set null [new Agent/Null]
$ns attach-agent $n3 $null

$ns connect $udp $null

set cbr [new Application/Traffic/CBR]
$cbr attach-agent $udp
$cbr set packet_size_ 1000
$cbr set rate_ 1Mb

$ns at 0.5 "$cbr start"
$ns at 4.5 "$cbr stop"

proc finish {} {
    global ns nf
    $ns flush-trace
    close $nf
    exec nam bus.nam &
    exit 0
}

$ns at 5.0 "finish"

$ns run
