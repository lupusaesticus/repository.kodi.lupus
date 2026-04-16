import os
import hashlib
import shutil

def generate_manifest():
    DEST_FOLDER = "repository.kodi.lupus"
    xml_content = u'<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n<addons>\n'
    for root, dirs, files in os.walk("."):
        for file in files:
            if file == "addon.xml" and "zips" in root:
                with open(os.path.join(root, file), "r", encoding="utf-8") as f:
                    lines = f.readlines()[1:]
                    xml_content += "".join(lines) + "\n"
    xml_content += u"</addons>\n"
    
    with open("addons.xml", "w", encoding="utf-8") as f:
        f.write(xml_content)
    
    md5_hash = hashlib.md5(xml_content.encode("utf-8")).hexdigest()
    with open("addons.xml.md5", "w", encoding="utf-8") as f:
        f.write(md5_hash)
    print("Manifest generated successfully.")

    # 3. Move them to the repo subfolder
    if not os.path.exists(DEST_FOLDER):
        os.makedirs(DEST_FOLDER)
        
    shutil.move("addons.xml", os.path.join(DEST_FOLDER, "addons.xml"))
    shutil.move("addons.xml.md5", os.path.join(DEST_FOLDER, "addons.xml.md5"))
    
    print(f"Manifest and MD5 successfully moved to {DEST_FOLDER}/")

if __name__ == "__main__":
    generate_manifest()