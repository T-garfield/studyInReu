/******************************************************************************

Online C# Compiler.
Code, Compile, Run and Debug C# program online.
Write your code in this editor and press "Run" button to execute it.
#1
clothes='домашняя одежда'
meal='мясо'
print('У меня большой гардероб.' '\n'
'Утром лучше всего подходит',clothes, '\n'
'Днем лучше всего подходит',clothes, '\n'
'Вечером лучше всего подходит',clothes, '\n'
'Ночью лучше всего подходит',clothes) 
print('Мои предпочтения в еде.' , '\n'
'Для завтрака лучше всего подходит',meal, '\n'
'Для обеда всего подходит',meal, '\n'
'Для ужина лучше всего подходит',meal)
#2
quilt_width=8
quilt_length=12
print(quilt_width*quilt_length)

quilt_width=8
quilt_length=8
print(quilt_width*quilt_length)

rectangle_w=23
rectangle_l=13
print(rectangle_w*rectangle_l)
*******************************************************************************/

using System;

abstract class AbstractHandler {
public abstract void Open();
public abstract void Create();
public abstract void Change();
public abstract void Save();
}

class XMLHandler: AbstractHandler {
public override void Open() {
Console.WriteLine("Opend XML file");
}
public override void Create() {
Console.WriteLine("Created XML file");
}
public override void Change() {
Console.WriteLine("Changed XML file");
}
public override void Save() {
Console.WriteLine("Saved XML file");
}
}

class TXTHandler: AbstractHandler {
public override void Open() {
Console.WriteLine("Opend TXT file");
}
public override void Create() {
Console.WriteLine("Created TXT file");
}
public override void Change() {
Console.WriteLine("Changed TXT file");
}
public override void Save() {
Console.WriteLine("Saved TXT file");
}
}

class DOCHandler: AbstractHandler {
public override void Open() {
Console.WriteLine("Opend DOC file");
}
public override void Create() {
Console.WriteLine("Created DOC file");
}
public override void Change() {
Console.WriteLine("Changed DOC file");
}
public override void Save() {
Console.WriteLine("Saved DOC file");
}
}
class Program {
static void Main() {
Console.WriteLine("Input file: ");
string file = Console.ReadLine();

switch (file){
case "XML":
XMLHandler XMLeditor = new XMLHandler();
XMLeditor.Open();
XMLeditor.Change();
XMLeditor.Save();
XMLeditor.Create();
break;
case "DOC":
DOCHandler DOCeditor = new DOCHandler();
DOCeditor.Open();
DOCeditor.Change();
DOCeditor.Save();
DOCeditor.Create();
break;
case "TXT":
TXTHandler TXTeditor = new TXTHandler();
TXTeditor.Open();
TXTeditor.Change();
TXTeditor.Save();
TXTeditor.Create();
break;
default:
Console.WriteLine("This file type doesn't suppoted");
break;
}
}
}