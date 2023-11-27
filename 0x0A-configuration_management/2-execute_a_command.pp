# Kill the process named "killmenow" using pkill

exec = {
    command => '/usr/lib/pkill -f killmenow',
    refreshonly => true
    onlyif => '/usr/bin/pgrep -f killmenow',
}
