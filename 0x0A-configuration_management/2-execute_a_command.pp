# Kill the process named "killmenow" using pkill

exec { 'pkil killmenow':
    path    =>  '/usr/bin/'
    command =>  'pkill killmenow',
    provider => shell,
    returns => [0, 1]
}
