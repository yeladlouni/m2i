class Capital2 {
  def show(country: String): Unit = {
    var capital = Map("US" -> "Washington", "France" -> "Paris")
    capital += ("Japan" -> "Tokyo")
    println(capital(country))
  }
}

object Example extends App {
  var capital2 = new Capital2()
  capital2.show("US")
}
