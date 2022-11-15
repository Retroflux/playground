use std::net::TcpStream;
use std::io::Write;
use std::{thread, time};


fn main(){

   let mut stream = TcpStream::connect("127.0.0.1:2048")
   .expect("Couldn't connect to the server...");
   let return_value = stream.write(b"Hello server from client\n");
   println!("Return value {:?}", return_value);
   let return_value = stream.write(b"Hello server from client\n");
   println!("Return value {:?}", return_value);
   let return_value = stream.write(b"Hello server from client\n");
   let ten_millis = time::Duration::from_millis(10000);
   thread::sleep(ten_millis);
   println!("Return value {:?}", return_value);
}