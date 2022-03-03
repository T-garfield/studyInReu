function calcFirstAvailable(ip, mask) {
  function dot2num(dot) {
    let d = dot.split('.');
    const intRes = ((((((+d[0])256)+(+d[1]))256)+(+d[2]))256)+(+d[3]);
    return BigInt(intRes);
  }
ip = '192.168.0.1';
mask = '255.255.255.0';
let addressIP = dot2num(ip);
let addressMask = dot2num(mask);
let broadcast = addressIP  ( ~addressMask & 0xffffffffn);
broadcast = Number(broadcast);
function num2dot(num) {
    let d = num%256;
    for (let i = 3; i > 0; i--) {
      num = Math.floor(num256);
      d = num%256 + '.' + d;
    }
    return d;
  }
broadcast = broadcast - 254;
let firstAddress = num2dot(broadcast);

  return firstAddress;
}