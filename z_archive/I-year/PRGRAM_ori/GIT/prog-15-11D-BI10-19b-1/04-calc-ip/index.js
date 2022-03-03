// вычисляет сетевой адрес
function calcNetworkAddress(ip, mask) {
  console.log ('fubction calcNetworkAddress: ip:', ip);
  console.log ('fubction calcNetworkAddress: mask:', mask);
  const BigInt = ip&mask;
  return num2dot (`${BigInt}`);
}
function calcNetworkAddress(ip, mask) { 
  console.log ('fubction calcNetworkAddress: ip:' , ip); 
  console.log ('fubction calcNetworkAddress: mask:', mask); 
  const BigInt = ip & mask 
  return num2dot(`${BigInt}`);
  }


// Вычисляет широковещательный адрес сети
function calcNetworkBroadcast(ip, mask) {
  //function calcNetworkBroadcast(ip, mask) {
  console.log('Данные ip и mask', ip, mask);
  let shir;
  shir = ip | (~mask & 0xffffffffn);
  shir = num2dot( Number(shir) );
  return shir;
  console.log(shir);
  //}
}

// Вычисляет первый доступный IP адрес
function calcFirstAvailable(ip, mask) {
  return "Не реализовано";
}

// Вычисляет последний доступный IP адрес
function calcLastAvailable(ip, mask) {
  return "Не реализовано";
}

// Вычисляет число доступных IP адресов
function calcNumberAvailable(ip, mask) {
  return "Не реализовано";
}

// Определяет, находятся ли данные IP адреса в одной сети
// Возвращает true/false
function calcSameNetwork(ip1, mask1, ip2, mask2) {
  return "Не реализовано";
}


////////////////////////////////////////////////////////////////


// функция преобразует строку IP адреса (4 байта в десятичном представлении, разделенные точками) в числовое представление
function dot2num(dot) {
  var d = dot.split('.');
  const intRes = ((((((+d[0])*256)+(+d[1]))*256)+(+d[2]))*256)+(+d[3]);
  return BigInt(intRes);
}


// функция преобразует целое число в строку, представлюящую собой стандартное представление IP-адреса - строку, представляющую собой 4 байта в десятичном виде, разделенные точками
function num2dot(num) {
  var d = num%256;
  for (var i = 3; i > 0; i--) {
    num = Math.floor(num/256);
    d = num%256 + '.' + d;
  }
  return d;
}

// функция преобразует целое число в строку, представлюящую собой представление IP-адреса - 4 байта в двоичном виде, разделенные точками
function num2bin(num) {
  var d = num.toString(2);
  d = d.substr(0,8)+'.'+d.substr(8,8)+'.'+d.substr(16,8)+'.'+d.substr(24,8);
  return d;
}


function doCalc() {
  // первый IP адрес
  // document.getElementById('ip1')
  const ipDot1 = document.querySelector('#ip1').value;
  console.log('ipDot1:', ipDot1);
  const ipNum1 = dot2num(ipDot1);
  console.log('ipNum1:', num2bin(ipNum1));

  // первая маска сети
  const maskDot1 = document.querySelector('#mask1').value;
  console.log('maskDot1:', maskDot1);
  const maskNum1 = dot2num(maskDot1);
  console.log('maskNum1:', num2bin(maskNum1));

  // второй IP адрес
  const ipDot2 = document.querySelector('#ip2').value;
  console.log('ipDot2:', ipDot2);
  const ipNum2 = dot2num(ipDot2);
  console.log('ipNum2:', num2bin(ipNum2));

  // вторая маска сети
  const maskDot2 = document.querySelector('#mask2').value;
  console.log('maskDot2:', maskDot2);
  const maskNum2 = dot2num(maskDot2);
  console.log('maskNum1:', num2bin(maskNum2));

  // вызов функций, вычисляющих требуемые значения

  document.querySelector('#network1').value = calcNetworkAddress(ipNum1, maskNum1);
  
  document.querySelector('#broadcast1').value = calcNetworkBroadcast(ipNum1, maskNum1);

  document.querySelector('#ipFirstAvail').value = calcFirstAvailable(ipNum1, maskNum1);

  document.querySelector('#ipLastAvail').value = calcLastAvailable(ipNum1, maskNum1);

  document.querySelector('#numAvail').value = calcNumberAvailable(ipNum1, maskNum1);

  document.querySelector('#sameNet').value = calcSameNetwork(ipNum1, maskNum1, ipNum2, maskNum2);
}
