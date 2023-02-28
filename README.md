<h3>Script para obtenção de coordenadas de endereços</h3>
Este script em Python foi desenvolvido com o objetivo de obter as coordenadas de latitude e longitude de uma lista de endereços contida em um arquivo CSV. Para isso, é utilizado o pacote Geopy, que faz uso do serviço de geocodificação gratuito do OpenStreetMap, o Nominatim. As coordenadas obtidas são adicionadas como colunas ao arquivo original e, em seguida, salvas em um novo arquivo CSV.

<h4>Pré-requisitos</h4>
Python 3.x <br>
Bibliotecas pandas e geopy instaladas <br>

<h4>Instruções de uso</h4>
Coloque o arquivo CSV contendo a lista de endereços na mesma pasta que o script Python. <br>
No início do script, defina o nome do arquivo CSV contendo os endereços e o nome que deseja dar ao arquivo de saída que será gerado.

<h4>Execute o script.</h4>
O arquivo de saída será gerado na mesma pasta que o script Python com o nome definido por você no passo 2.

<h4>Observações</h4>
Caso um endereço não seja encontrado, as colunas de latitude e longitude receberão a string 'Endereço não encontrado'. <br>
O script faz uso do serviço gratuito de geocodificação do OpenStreetMap, o que pode limitar o número de consultas realizadas em um curto período de tempo. Caso precise consultar muitos endereços, é recomendado adquirir uma chave de API de um serviço de geocodificação pago ou limitar a quantidade de endereços consultados de uma só vez.
