pub fn run() {
   let person: (&str, &str, i8) = ("Retroflux", "Canada", 37); 

   if person.0 == "Retroflux"{
      println!("{} is from {} and is giga-old (aka age: {})", person.0, person.1, person.2);
   }

}