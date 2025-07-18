from django.shortcuts import render

# Create your views here.
def index(request):
    inicio = {
        "titulo": "bem vindo ao meu projeto",
        "paragrafo": "este site é dedicado as mulheres proeminentes que se encontraram no meio politico brasileiro",
        "resumo": "o que voce encontrará aqui:",
        "importancia": "importância",
        "tempo": "tempo de mandato",
        "premiacao": "premiações"

    }
    footer = {
        "footer1": "site de joão emanuel"
    }
    return render(request, 'blog/index.html', {"inicio": inicio, "footer": footer})

def mulheres(request):

    mulheres = [

        {"nome": "Benedita da Silva", "idade": 83, "datanasc": "1942/04/23", "imagem": "blog/benedita.png", "nascimento": "morro do chapeu mangueira, rio de janeiro"},
        {"nome": "Marielle Franco", "idade": 38, "datanasc": "1979/07/27", "imagem": "blog/marielle.png", "nascimento": "complexo da maré, rio de janeiro"},
        {"nome": "Nísia Floresta", "idade": 75, "datanasc": "1810/10/12", "imagem": "blog/nisia.png", "nascimento": "papari, rio grande do norte" }
    ]
    return render(request, 'blog/mulheres.html', {"mulheres": mulheres})
def historia(request):

    historias = {
        "historia1": "Benedita da Silva nasceu em 1942 no Morro do Chapéu Mangueira, no Rio de Janeiro. Sua trajetória começou em condições humildes, trabalhando como doméstica, babá e auxiliar de enfermagem antes de se formar em Serviço Social. Sua entrada na política foi marcada pelo ativismo comunitário em favelas do Rio. Em 1982, tornou-se a primeira vereadora negra da cidade, eleita pelo PDT. Como deputada federal entre 1986 e 1994, participou da Assembleia Nacional Constituinte, onde lutou por direitos como licença-maternidade de 120 dias e a criminalização do racismo. Em 1994, foi eleita a primeira senadora negra do Brasil, cargo que ocupou até 2002. Em 2002, assumiu como governadora do Rio de Janeiro, tornando-se a primeira mulher negra a governar um estado brasileiro. No governo Lula, foi ministra da Secretaria de Promoção da Igualdade Racial, onde implementou políticas de inclusão social. Recebeu o Prêmio Bertha Lutz em 2001 por suas contribuições aos direitos das mulheres e a Medalha Zumbi dos Palmares em 2017. Em 2023, recebeu o título de Doutora Honoris Causa pela Universidade de Brasília. Sua trajetória inspirou gerações de mulheres negras e periféricas a entrar na política.",
        "historia2": "Marielle Franco nasceu em 1979 no Complexo da Maré, no Rio de Janeiro. Criada em uma comunidade carente, teve sua primeira filha aos 19 anos, mas continuou seus estudos, formando-se em Sociologia pela PUC-RJ e obtendo mestrado em Administração Pública pela UFF. Antes de entrar na política, trabalhou como assessora do deputado Marcelo Freixo, onde se destacou na denúncia de milícias e violência policial. Em 2016, foi eleita vereadora do Rio de Janeiro pelo PSOL com 46.502 votos, tornando-se a quinta mais votada. Durante seu mandato, foi relatora da Comissão da Mulher e autora de projetos como a Legislação Antirretificação, que buscava evitar alterações em autos de resistência, e o Programa de Proteção a Mães de Vítimas da Violência. Marielle tornou-se conhecida por suas críticas à intervenção federal no Rio de Janeiro em 2018 e por denunciar a ação de milícias. Em 14 de março de 2018, foi assassinada aos 38 anos em um atentado no centro do Rio, junto com seu motorista, Anderson Gomes. Seu crime, até hoje não completamente esclarecido, gerou comoção nacional e internacional. Recebeu postumamente o Prêmio de Direitos Humanos da ONU em 2017 e foi declarada Heroína da Liberdade pelo governo francês em 2018. Em 2019, a Universidade de Essex, no Reino Unido, concedeu-lhe o título de Doutora Honoris Causa. Em 2023, uma estátua em sua homenagem foi inaugurada no centro do Rio, sendo a primeira dedicada a uma mulher negra no espaço público carioca. Marielle se tornou um símbolo global da luta por justiça e democracia, inspirando candidaturas de mulheres negras e periféricas em todo o mundo.",
        "historia3": "Nísia Floresta nasceu em 1810 no Rio Grande do Norte, então chamado Papari, cidade que mais tarde receberia seu nome em homenagem. Seu nome de batismo era Dionísia Gonçalves Pinto. Ela se tornou uma das primeiras vozes feministas no Brasil, destacando-se como educadora e escritora em pleno século XIX, período marcado por uma sociedade extremamente conservadora. Nísia foi profundamente influenciada pelas ideias iluministas e dedicou sua vida a defender os direitos das mulheres, dos indígenas e dos escravizados. Em 1832, publicou Direitos das Mulheres e Injustiça dos Homens, considerado o primeiro livro feminista do Brasil, baseado nas obras de Mary Wollstonecraft. Além de suas contribuições literárias, Nísia fundou colégios para meninas no Rio de Janeiro e em Porto Alegre, promovendo a educação feminina em uma época em que as mulheres tinham acesso limitado ao conhecimento. Sua obra Opúsculo Humanitário abordava temas como abolicionismo e direitos indígenas, mostrando seu compromisso com causas sociais. Seu legado foi reconhecido postumamente, com cidades, escolas e centros de estudos de gênero recebendo seu nome. Em 2019, foi homenageada pelo Google Doodle, reforçando sua importância como pioneira do feminismo brasileiro."
    }
    politica = {
        "mulherpol": "Mulheres na politica Brasileira"
    }
    return render(request, 'blog/historia.html', {"historias": historias, "politica": politica})
