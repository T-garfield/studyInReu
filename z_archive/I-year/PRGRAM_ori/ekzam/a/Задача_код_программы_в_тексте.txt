var X=[26,28,-4]
var Y=[33,20,-3]
var A=0

console.log(X,Y)
for (var i=0;i<X.length; i++){
  if (X[i]<Y[i]){
    A=X[i]
    X[i]=Y[i]
    Y[i]=A
    
    /* без буфера
    X[i]+=Y[i]
    Y[i]=X[i]-Y[i]
    X[i]=X[i]-Y[i]
    */
  }
}
console.log('Result: ', X,Y)