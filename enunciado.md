Você recebeu duas páginas HTML prontas, já com CSS, de um site fictício chamado "Estúdio Fluxo": index.html, a página inicial, e portfolio.html, a página de portfólio, além da folha de estilos compartilhada em css/style.css. As duas páginas têm cabeçalho e rodapé idênticos — isso é proposital, pois é justamente essa parte repetida que você vai transformar em um template base ao longo da atividade.  
  
  
1. Crie um projeto Django novo e, dentro dele, um app com um nome apropriado. Configure a pasta de templates do projeto e organize a estrutura de pastas de template dentro do app, do jeito que foi mostrado em aula.  
  
2. Observe as duas páginas fornecidas e identifique o que se repete entre elas e o que é exclusivo de cada uma. Com base nisso, crie um base.html. Depois, crie um template para a Home e outro para o Portfólio, cada um estendendo o base.html e preenchendo esse bloco com o conteúdo correspondente.  
  
3. Crie também as views e as rotas em [urls.py](http://urls.py) para as duas páginas. Troque todos os links de navegação entre as páginas para usar {% url 'nome-da-rota' %} em vez de apontar diretamente para o arquivo .html. Por fim, mova o CSS para a pasta static/ do projeto e ajuste o &lt;link&gt; das páginas para carregar o arquivo estático.  
  
Ao final, rode o projeto  e confirme que as duas páginas abrem corretamente com o CSS aplicado, que a navegação entre Home e Portfólio funciona através dos links e que não sobrou nenhum caminho de arquivo ou link fixo apontando para .html.  
  
Todo o desenvolvimento desta atividade deve ser versionado com Git, seguindo o fluxo do GitFlow. Adicione um .gitignore adequado para projetos Django/Python.  
  
Para cada etapa da atividade, crie uma branch separada a partir de develop, com o prefixo "feature/". Uma divisão possível é: feature/estrutura-projeto para a criação do projeto e do app Django, feature/template-base para a criação do base.html, feature/pagina-home e feature/pagina-portfolio para o template e a rota de cada página, feature/navegacao-url para a troca dos links por {% url %}, e feature/arquivos-estaticos para a configuração do CSS como arquivo estático.