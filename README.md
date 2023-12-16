# Playing with benchmarks

crated a fast api server in python that reads all items from a sqlite db and returns them as json

then created a golang client that makes requests in batches

this was a test on my local machine(macbook pro m1)

with 100 request per bach and 1000 batches all requests succed which was impresive

with 150 request per 100 bathches most request succesd only around 150 failed
