var Client = require('lib/ssh2/client').Client;
var fs = require('fs');
var html2json = require('html2json').html2json;
var netdata = require("netdata");
const nodeprocess = require('process');


// the processor is needed only
// if you need a custom processor
// other than http
netdata.processors.powertop = {
	name: 'powertop',

	process: function(service, callback) {

		// if (!shell.which('powertop')) {
        //     shell.echo('Sorry, this script requires powertop');
        //     shell.exit(1);
        // } else{
        //     shell.echo('Switching user...');
        //     shell.exec('echo felouka | su ricknmorty')
        //     powerOut = shell.exec('echo felouka | sudo -S powertop --time=1 --html="./powertop.html"')
        //     if (powerOut.code !== 0) {
        //         shell.echo('Error: powertop command failed');
        //         shell.exit(1);
        //     } else{
        //         res = []
        //         fs.readFile('./powertop.html', 'utf8', function(err, data){
        //             var doc = html2json(data)
        //             var rows = doc.child[0].child[3].child[16].child[3].child;
                    
        //             for(var i = 1; i < rows.length; i+=2){
        //                 row = rows[i].child
        //                 usage = row[1].child[0].text.trim()
        //                 category = row[row.length - 4].child[0].text.trim()
        //                 desc = row[row.length - 2].child[0].text.trim()
        //                 if(category == "Process"){
        //                     pid = desc.match(/[0-9]+/g)[0]
        //                     microsec = usage.match(/us/g)
        //                     value = parseFloat(usage.match(/[0-9]+\.[0-9]+/g))
        //                     if (microsec != null){
        //                         value = value/1000
        //                     }
        //                     res.push({pid, value})
        //                 }
        //             }
        //             callback(res)     
        //         })
        //     }
        // }

        var conn = new Client();
        conn.on('ready', function() {
            netdata.debug('Client :: ready');
            netdata.debug('Node version is: ' + nodeprocess.version);
            conn.exec('echo felouka | sudo -S powertop --time=1 --html="./powertop.html"', function(err, stream) {
                if (err) {
                    netdata.debug("ERROR EXEC COMMAND: " + err)
                    throw err;
                }
                stream.on('close', function(code, signal) {
                    res = []
                    fs.readFile('/home/ricknmorty/powertop.html', 'utf8', function(err, data){
                        if (err) {
                            netdata.debug("ERROR READING HTML: " + err)
                            throw err;
                        }
                        var doc = html2json(data)
                        var rows = doc.child[0].child[3].child[16].child[3].child;
                        
                        for(var i = 1; i < rows.length; i+=2){
                            row = rows[i].child
                            usage = row[1].child[0].text.trim()
                            category = row[row.length - 4].child[0].text.trim()
                            desc = row[row.length - 2].child[0].text.trim()
                            if(category == "Process"){
                                pid = desc.match(/[0-9]+/g)[0]
                                microsec = usage.match(/us/g)
                                value = parseFloat(usage.match(/[0-9]+\.[0-9]+/g))
                                if (microsec != null){
                                    value = value/1000
                                }
                                res.push({pid, value})
                            }
                        }
                        netdata.debug("Returning: " + res)
                        // conn.end();
                        callback(res)    
                    })
                    
                }).on('data', function(data) {
                    // console.log('STDOUT: ' + data);
                });
                
            });
        }).connect({
            host: 'localhost',
            username: 'ricknmorty',
            password: 'felouka'
        });

		// callback(null);
	}
};

// this is the powertop definition
var powertop = {
	processResponse: function(service, data) {
        netdata.debug("Process Response")
        /* send information to the Netdata server here */
        if (data === null) {
            return;
        }
        // if(service.added !== true)
        service.commit();

        dims = {}
        data = data.sort(function (a, b) {
            return b.value - a.value;
        });
        for (var i = 0; i < data.length && i < 6; i++){
            process = data[i]
            dims[process.pid] =  {
                id: process.pid,                                     // the unique id of the dimension                       
                hidden: false                               // is hidden (boolean)
            };
        }

        chart = {
            id: "powertop",                                     // the unique id of the chart
            name: "powertop",                                        // the unique name of the chart
            title: "Power top processes percentage power consumption",// the title of the chart
            units: "ms/s",                                      // the units of the chart dimensions
            family: "powertopcharts",                             // the family of the chart
            context: "powertop.processes.output",              // the context of the chart
            type: netdata.chartTypes.area,                // the type of the chart
            priority: 6000,             // the priority relative to others in the same family
            update_every: service.update_every,
            dimensions: dims           // the expected update frequency of the chart
        };
        netdata.debug("Starting response...")
        chart = service.chart("powertop", chart);
        service.begin(chart);
        for (var i = 0; i < data.length && i < 6; i++){
            process = data[i]
            // netdata.debug("Adding to chart: " + process.pid + " " + process.value)
            service.set(process.pid, process.value)

        }
        netdata.debug("Ending response...")
        service.end();
        netdata.debug("Ending Service...")

	},

	configure: function(config) {
        netdata.debug("Configure")
        /*
            * create a service using internal defaults;
            * this is used for auto-detecting the settings
            * if possible
            */

        netdata.service({
            name: 'powertop',
            update_every: this.update_every,
            module: this,
            processor: netdata.processors.powertop,
            // any other information your processor needs
        }).execute(this.processResponse);


		return 1;
	},

	update: function(service, callback) {
		netdata.debug("update")
		/*
		 * this function is called when each service
		 * created by the configure function, needs to
		 * collect updated values.
		 *
		 * You normally will not need to change it.
		 */

        service.execute(function(serv, data) {
            service.module.processResponse(serv, data);
            callback();
        });
	},
};

module.exports = powertop;