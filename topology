# Create simulator
set ns [new Simulator]

# Open NAM file
set nf [open bus.nam w]
$ns namtrace-all $nf

# Create nodes
set n0 [$ns node]
set n1 [$ns node]
set n2 [$ns node]
set n3 [$ns node]

# Bus topology (line)
$ns duplex-link $n0 $n1 1Mb 10ms DropTail
$ns duplex-link $n1 $n2 1Mb 10ms DropTail
$ns duplex-link $n2 $n3 1Mb 10ms DropTail

# Create UDP agent
set udp [new Agent/UDP]
$ns attach-agent $n0 $udp

# Create Null agent (receiver)
set null [new Agent/Null]
$ns attach-agent $n3 $null

# Connect agents
$ns connect $udp $null

# Create traffic
set cbr [new Application/Traffic/CBR]
$cbr attach-agent $udp
$cbr set rate_ 1Mb

# Start and stop traffic
$ns at 1.0 "$cbr start"
$ns at 4.0 "$cbr stop"

# Finish procedure
proc finish {} {
    global ns nf
    $ns flush-trace
    close $nf
    exec nam bus.nam &
    exit 0
}

# End simulation
$ns at 5.0 "finish"

# Run
$ns run
