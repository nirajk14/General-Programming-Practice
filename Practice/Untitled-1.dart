//Since no constraints were given I am using all usable library functions
String reverseorder(String str) {
  List<String> a = str.split(' ');
  List<String> reva = new List.from(a.reversed);
  return reva.join(' ');
}

void main() {
  print(reverseorder("Hello World")); //Feel free to test with any string
}
