""" BLOCKCHAIN SAMPLE """
from hashlib import sha256


class NewCoinBlock:

    def __init__(self, block_number, previous_block_hash, transaction_list):

        self.block_number = block_number
        self.previous_block_hash = previous_block_hash
        self.transaction_list = transaction_list

        self.block_data = f"{' -> '.join(transaction_list)} / {previous_block_hash}"
        self.block_hash = sha256(self.block_data.encode()).hexdigest()

    blocks_list = list()
    current_transactions_list = list()
    block_number = 1

    @staticmethod
    def new_transaction():

        sender = input('Отправитель: ')
        recipient = input('Получатель: ')
        amount = input('Количесвто монет: ')

        NewCoinBlock.current_transactions_list.append(f'{sender} sends {amount} NC to {recipient}')

        if len(NewCoinBlock.current_transactions_list) == 3:

            if NewCoinBlock.block_number > 1:
                block = NewCoinBlock(block_number=NewCoinBlock.block_number,
                                     previous_block_hash=NewCoinBlock.blocks_list[NewCoinBlock.block_number-2].block_hash,
                                     transaction_list=NewCoinBlock.current_transactions_list)
            else:
                block = NewCoinBlock(block_number=NewCoinBlock.block_number,
                                     previous_block_hash='firstblock',
                                     transaction_list=NewCoinBlock.current_transactions_list)

            NewCoinBlock.blocks_list.append(block)
            NewCoinBlock.current_transactions_list = []
            NewCoinBlock.block_number += 1

        print('Транзакция добавлена!')


# Действия пользователя
while True:

    user_input = input('Что вы хотите сделать?\n[1]: добавить транзакцию\n[2]: посмотреть список текущих транзакций\n'
                       '[3]: посмотреть список всех блоков\n[0]: выйти\n')

    if user_input == '1':
        NewCoinBlock.new_transaction()

    elif user_input == '2':
        if len(NewCoinBlock.current_transactions_list) > 0:
            print(' -> '.join(NewCoinBlock.current_transactions_list))
        else:
            print('Список текущих транзакций пуст.')

    elif user_input == '3':
        for block in NewCoinBlock.blocks_list:
            print(f'Block {block.block_number}:\n'
                  f'{block.block_data}\n')

    elif user_input == '0':
        break

    else:
        print("Такого действия нет. Выберите вариант 1, 2, 3 или 0.")

    print()