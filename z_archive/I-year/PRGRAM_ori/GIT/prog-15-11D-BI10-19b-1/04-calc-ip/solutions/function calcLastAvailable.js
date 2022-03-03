function calcLastAvailable(ip, mask) {
    function dot2num(dot) {
        var d = dot.split('.');
        const intRes = ((((((+d[0])*256)+(+d[1]))*256)+(+d[2]))*256)+(+d[3]);
        return BigInt(intRes);
      }
    let adresIP = dot2num(ip);
    let adresMask = dot2num(mask);
    let shirokovesh = adresIP | ( ~adresMask & 0xffffffffn);
    shirokovesh = Number(shirokovesh);
    function num2dot(num) {
        var d = num%256;
        for (var i = 3; i > 0; i--) {
          num = Math.floor(num/256);
          d = num%256 + '.' + d;
        }
        return d;
      }
    shirokovesh = shirokovesh - 1;
    let posledniyAdres = num2dot(shirokovesh);
    console.log(posledniyAdres);
  }