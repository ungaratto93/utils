from datetime import datetime

print('entrada: \r')
entrada = input()
print('saida_almoco: \r')
saida_almoco = input()
print('volta_almoco: \r')
volta_almoco = input()

entrada = datetime.strptime(entrada, '%H:%M')
saida_almoco = datetime.strptime(saida_almoco, '%H:%M')
horas_manha = (saida_almoco.hour - entrada.hour)
minutos_manha = (saida_almoco.minute - entrada.minute)
print('Trabalhado na manha:', str(horas_manha) + ':' + str(minutos_manha))
print('Preciso trabalhar ainda:', str(8-horas_manha) + ':' + str(48-minutos_manha))

horas_afazer = 8-horas_manha
minutos_afazer = 48-minutos_manha
volta_almoco = datetime.strptime(volta_almoco, '%H:%M')
hora_sair = horas_afazer + volta_almoco.hour
minutos_sair = minutos_afazer + volta_almoco.minute
print("Hora provavel de saída: ", str(hora_sair) + ":" + str(minutos_sair))