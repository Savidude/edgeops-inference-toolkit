use std::fs;
use std::io::copy;

#[tokio::main]
pub async fn download_from_url(url: &str, destination: &str) -> Result<(), Box<dyn std::error::Error>> {
    let response = reqwest::get(url).await?;
    let bytes = response.bytes().await?;
    let mut file = fs::File::create(destination)?;
    copy(&mut bytes.as_ref(), &mut file)?;
    Ok(())
}

pub fn unzip_file(zip_file_path: &str) {
    let file = fs::File::open(zip_file_path).unwrap();
    let mut archive = zip::ZipArchive::new(file).unwrap();

    for i in 0..archive.len() {
        let mut file = archive.by_index(i).unwrap();
        let outpath = match file.enclosed_name() {
            Some(path) => path.to_owned(),
            None => continue,
        };

        if (*file.name()).ends_with('/') {
            fs::create_dir_all(&outpath).unwrap();
        } else {
            if let Some(p) = outpath.parent() {
                if !p.exists() {
                    fs::create_dir_all(p).unwrap();
                }
            }
            let mut outfile = fs::File::create(&outpath).unwrap();
            copy(&mut file, &mut outfile).unwrap();
        }
    }
}

pub fn rename(src: &str, dest: &str) -> std::io::Result<()> {
    fs::rename(src,dest)?; // Rename a.txt to b.txt
    Ok(())
}
