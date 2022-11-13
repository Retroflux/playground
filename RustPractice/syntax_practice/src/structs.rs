mod person;

//Traditional structure
struct Colour{
   red : u8,
   green : u8,
   blue : u8
}

//Tuple Structure
struct TupleColour(u8,u8,u8);




pub fn run(){

   let mut c = Colour{red: 255, green: 0, blue: 0};
   println!("\nStructs begin here:");
   println!("I made a red colour struct: {} {} {}", c.red, c.blue, c.green);

   c.red = 200;
   println!("I made a slightly less red colour struct: {} {} {}", c.red, c.blue, c.green);

   let mut tuple_colour = TupleColour(255,0 , 0);
   tuple_colour.1 = 255;
   tuple_colour.2 = 255;
   println!("I made a white(?) colour struct: {} {} {}", tuple_colour.0, tuple_colour.1, tuple_colour.2);

   let mut individual_person = person::Person::new("Harry","Styles");

   println!("New Person created: {} {}",individual_person.get_first_name(), individual_person.get_last_name());

   println!("Full name: {}", individual_person.get_full_name());

   individual_person.set_first_name("new_first");
   individual_person.set_last_name("new_last");

   println!("Tuple after a name change: {:?}", individual_person.to_tuple());

}