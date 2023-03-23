use crate::constants;
use crate::util::files;

fn download_project_template() -> String {
    let version: &str = env!("CARGO_PKG_VERSION");
    let template_download_path = format!("{}/{}", "/tmp", constants::PROJECT_TEMPLATE_ZIP);
    let template_url: String = format!("{}/v{}/{}", constants::GITHUB_PROJECT_RELEASES_URL, version, constants::PROJECT_TEMPLATE_ZIP);
    if let Err(e) = files::download_from_url(&template_url, &template_download_path) {
        print!("Error while downloading file {}", e);
    }
    return template_download_path;
}

fn unzip_template_file(template_path: &str, project_name: &str) {
    files::unzip_file(template_path);
    match files::rename(constants::PROJECT_TEMPLATE_DIR, project_name) {
        Ok(()) => print!("Template file renamed!"),
        Err(_) => print!("Error while renaming template file"),
    }
}

pub fn initialize(project_name: &str) {
    print!("Downloading template file");
    let template_path: String = download_project_template();
    unzip_template_file(&template_path, project_name);
}