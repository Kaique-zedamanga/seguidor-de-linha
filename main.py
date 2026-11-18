def on_forever():
    # Lê os sensores esquerdo e direito (0 = encontrou a linha preta, 1 = fora da linha / branco)
    left_sensor = maqueen.read_patrol(maqueen.Patrol.PATROL_LEFT)
    right_sensor = maqueen.read_patrol(maqueen.Patrol.PATROL_RIGHT)

    # Ambos na linha: vai para frente
    if left_sensor == 0 and right_sensor == 0:
        maqueen.motor_run(maqueen.Motors.M1, maqueen.Dir.CW, 200)
        maqueen.motor_run(maqueen.Motors.M2, maqueen.Dir.CW, 200)
    
    # Apenas o esquerdo saiu da linha: vira para a direita
    elif left_sensor == 1 and right_sensor == 0:
        maqueen.motor_run(maqueen.Motors.M1, maqueen.Dir.CW, 200)
        maqueen.motor_run(maqueen.Motors.M2, maqueen.Dir.CW, 0)
    
    # Apenas o direito saiu da linha: vira para a esquerda
    elif left_sensor == 0 and right_sensor == 1:
        maqueen.motor_run(maqueen.Motors.M1, maqueen.Dir.CW, 0)
        maqueen.motor_run(maqueen.Motors.M2, maqueen.Dir.CW, 200)
    
    # Ambos fora da linha: para ou busca
    else:
        maqueen.motor_run(maqueen.Motors.M1, maqueen.Dir.CW, 0)
        maqueen.motor_run(maqueen.Motors.M2, maqueen.Dir.CW, 0)

basic.forever(on_forever)