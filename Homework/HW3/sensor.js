var sensor = require('node-dht-sensor');
var temp = [];
var sum_temp = 0;
var hum = [];
var sum_hum = 0
var avg_temp = 0
var avg_hum = 0
sensor.read(22, 4, function(err, temperature, humidity) 
{
    if (!err) 
    {
	for(i = 1; i < 11; i++)
	{
	    temp[i] = ((temperature*1.8)+32).toFixed(1);
	    hum[i] = humidity.toFixed(1);
	    sum_temp = (sum_temp + +temp[i]);
	    sum_hum = (sum_hum + +hum[i]);
     	    console.log( i + ' Temp: ' + ((temperature*1.8)+32).toFixed(1) + ' degF, ' + humidity.toFixed(1) + '% Hum');
	}
	console.log('Lowest Temp ' + Math.min(temp[1],temp[2],temp[3],temp[4],temp[5],temp[6],temp[7],temp[8],temp[9],temp[10]) + ' degF');
	console.log('Lowest Hum ' + Math.min(temp[1],temp[2],temp[3],temp[4],temp[5],temp[6],temp[7],temp[8],temp[9],temp[10]) + '%');
	console.log('Highest Temp ' + Math.max(temp[1],temp[2],temp[3],temp[4],temp[5],temp[6],temp[7],temp[8],temp[9],temp[10]) + ' degF');
	console.log('Highest Hum ' + Math.max(temp[1],temp[2],temp[3],temp[4],temp[5],temp[6],temp[7],temp[8],temp[9],temp[10]) + '%');
	console.log('Average Temp: ' + (sum_temp/10).toFixed(1) + ' degF');
	console.log('Average Hum: ' + (sum_hum/10).toFixed(1) + '%');
    }	    
});