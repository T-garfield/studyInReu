var X=[7,3,6,5,-1,-8]
var Y=[4,8,7,3,3,-5]
var buf=0
console.log(X,Y)
for (var i=0;i<X.length; i++){
  if (X[i]<Y[i]){
    buf=X[i]
    X[i]=Y[i]
    Y[i]=buf
    /* без буфера
    X[i]+=Y[i]
    Y[i]=X[i]-Y[i]
    X[i]=X[i]-Y[i]*/
  }
}
console.log('Result: ' + X,Y)