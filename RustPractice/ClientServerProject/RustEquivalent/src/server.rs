use std::io::Read;
use std::env;
use std::net::Shutdown;
use std::net::TcpListener;
use std::net::TcpStream;

// const DEFAULTTHREADSIZE: u16 = 2048;
static DEFAULTPORTNUM: u16 = 2048;

// struct ThreadArgs{
//     worker_id : u32,
//     thread_val : u32
// }

// struct FileInformation{
//     total_file_size : u128,
//     total_received : u128,
//     worker_id : u32,
//     name_of_file : String
// }


fn handle_client(stream: &mut TcpStream){

    let mut buffer = [0;10];
    println!("{:?}",stream.peer_addr());
    println!("Peeked content: {}", stream.peek(&mut buffer).expect("peek failed"));
    loop{
        let read_value = stream.read(&mut buffer);
        if let Err(_) = &read_value{
            println!("ERROR");
            break;
        }        
        if let Ok(0) = &read_value{
            println!("EOF Reached");
            break;
        }
        if let Ok(_) = &read_value{
            let s = std::str::from_utf8(&buffer).unwrap();
            println!("Buffer: {:?}", s);
        }
    }
    stream.shutdown(Shutdown::Both).expect("shutdown call failed");
}


fn main() -> std::io::Result<()> {

    let args: Vec<String> = env::args().collect();
    let mut port_number = DEFAULTPORTNUM;
    if args.len() == 2 {
        println!("no port number specified: starting on port 2048");
    }else if args.len() == 3{
        println!("{} will be used as the port number", args[2]);
        port_number = args[2].parse::<u16>().unwrap();
    }  
    println!("Port number: {}", port_number);
    let mut receiving_address = String::from("127.0.0.1:");
    receiving_address.push_str(&port_number.to_string());

    let listener = TcpListener::bind(receiving_address)?;

    for stream in listener.incoming() {
        handle_client(&mut stream?);
    }

    Ok(())
}
