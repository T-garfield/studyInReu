function LineSearch
(Key: ItemType, n: integer; var A: array[1..n] of ItemType): boolean;
{Ham tim kiem tuan tu}
{Neu khong tim thay phan tu, tra lai gia tri "True", nguoc lai - "False"}
var i: integer;
begin
	i:=1;
	while (i <= n) and (A[i]<>Key) do i := i + 1;
	if A[i] = Key then LineSearch := true
					else LineSearch := false;
end;




program primer2_2802
function LineSearchWithBarrier
(Key: ItemType, n: integer; var A: array[1..n+1] of ItemType): boolean;
{Функция линейного поиска с барьером,}
{если элемент найден, то возвращает значение true, иначе - false}
var i: integer;
begin
	I:=1;
	A[n+1] := key;
	while A[i] <> key do I := I + 1;
	if I <= n then LineSearchWithBarrier := true
	else LineSearchWithBarrier := false;
end;

