const getPressure = async () => {
const url = 'https://www.gismeteo.ru/weather-moscow-4368/';
let rawHtml;
try {
rawHtml = await axios.get(url);
} catch (error) {
console.log('error while getting web: ', error);
return error;
}
const $ = cheerio.load(rawHtml.data);
const pressureNode = $('.unit.unit_pressure_mm_hg_atm');
debugger;
return pressureNode[2].children[0].data;
}(async () => {
console.log('Давление: ',await getPressure());
})();
