from pathlib import Path
import uuid
import qrcode

# STATUS -> PENDENTE ou PAGO

# dados -> chave pix (da empresa), valor, descricao, status

def gerarQrCodePixCobranca(cliente, dados):
    identificador = str(uuid.uuid1())
    
    pasta = Path("arquivos/qrcodes/cobrancas") / cliente["nome"]
    pasta.mkdir(parents=True, exist_ok=True)
    arquivo = pasta / f"pagamento_{identificador}.png"
    
    img = qrcode.make(dados)
    
    img.save(arquivo)
    
    print(f"QR Code da cobrança gerado em: {arquivo}")
    
    return arquivo

# dados -> chave pix da empresa, chave pix do cliente, valor, descricao, status

def gerarQrCodeComprovante(cliente, dados):
    identificador = str(uuid.uuid1())
    
    pasta = Path("arquivos/qrcodes/comprovantes") / cliente["nome"]
    pasta.mkdir(parents=True, exist_ok=True)
    arquivo = pasta / f"pagamento_{identificador}.png"
    
    img = qrcode.make(dados)
    
    img.save(arquivo)
    
    print(f"QR Code do comprovante gerado em: {arquivo}")
    
    return arquivo