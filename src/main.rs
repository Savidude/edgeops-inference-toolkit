use clap::{Args, Parser, Subcommand};

mod cmd;
mod constants;

mod util {
    pub mod files;
}

#[derive(Parser)]
#[command(author, version, about, long_about = None)]
#[command(propagate_version = true)]
struct Cli {
    #[command(subcommand)]
    command: Commands,
}

#[derive(Subcommand)]
enum Commands {
    /// Initialize the model inference handler
    Init(Init)
}

#[derive(Args)]
struct Init {
    /// Name of the model inference project
    project_name: String
}

fn main() {
    let cli = Cli::parse();
    match &cli.command {
        Commands::Init(init) => {
            cmd::init::initialize(&init.project_name);
        }
    }

}
