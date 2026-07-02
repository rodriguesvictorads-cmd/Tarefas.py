import os
import shutil

def mover_arquivo(arquivo, pasta_destino):
   pasta_destino = os.path.join(
      pasta,
      pasta_destino
    )
    os.makedirs(
        pasta_destino,
        exist_ok = True
    )
      
      caminho_destino = os.path.join
    )
     shutil.move(
         caminho_destino,
         os.path.join(
            pasta_destino,
            arquivo
         )
   )
   print (arquivo, "movido!")
pasta = r"C:\Users\Admin\Downloads"

for arquivo in os.listdir(pasta):
    extensao = os.path.splitext(arquivo)[1].lower()
    print(arquivo, "->", extensao)

    if extensao == ".pdf":
        pasta_destino = os.path.join(
            pasta, 
             "PDFs"
        )
        os.makedirs(
            pasta_destino,
            exist_ok = True
        )

        caminho_arquivo = os.path.join(
             pasta,
             arquivo
        )
        shutil.move(
            caminho_arquivo,
            os.path.join(
                pasta_destino,
                arquivo
            )
        )
        print(arquivo,"movido!")
    elif extensao == ".png":
        pasta_destino = os.path.join(
            pasta,
            "Imagens"
        )
        os.makedirs(
            pasta_destino,
            exist_ok = True
        )
        
        caminho_arquivo = os.path.join(
             pasta,
             arquivo
        )
        shutil.move(
            caminho_arquivo,
            os.path.join(
                pasta_destino,
                arquivo
            )
        )
        print(arquivo,"movido!")
    elif extensao == ".jpg":
        pasta_destino = os.path.join(
            pasta,
            ".jpgs"
        )
        os.makedirs(
            pasta_destino,
            exist_ok = True
        )
        caminho_arquivo = os.path.join(
            pasta,
            arquivo
        )
        shutil.move(
            caminho_arquivo,
            os.path.join(
                pasta_destino,
                arquivo
            )
        )
        print (arquivo, "movido!")
