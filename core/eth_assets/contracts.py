#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Import Console_Constant: STRING_DASHES
from core.constants.console_constant import STRING_DASHES


class ContractArtifacts:
    """ Contract Artifacts
    This class will store all the information regarding contract_cli eth_assets
    """
    def __init__(self, logger):
        self.logger = logger
        self.contract_data = {}

    def pre_load_contract_artifacts(self, contract_address, contract_abi):
        """ Pre Load Contract Artifacts
        This function will pre-load any provided contract_cli artifact, during the launching process of the general console
        gnosis-cli.
        :param contract_address:
        :return:
        """
        if contract_address:
            self.logger.debug0('')
            self.logger.debug0(' | Setup Contract Artifacts  | ')
            self.logger.debug0(STRING_DASHES)
            for artifact in contract_address:
                self.logger.debug0('(+) Contract Artifact [ {0} with Address {1} ]'.format(
                    artifact['name'], artifact['address'])
                )
                self.add_contract_artifact(
                    artifact['name'], artifact['instance'], artifact['abi'],
                    artifact['bytecode'], artifact['address'], (artifact['name'] + '_' + str(len(self.contract_data)))
                )
            self.logger.debug0(STRING_DASHES)
            self.logger.debug0('')

    def command_view_contracts(self):
        """ Command View Contracts
        This function will show the values currently stored withing he contract_cli artifact class
        :return:
        """
        abi_status = False
        bytecode_status = False

        self.logger.info(' ' + STRING_DASHES)
        self.logger.info('| {0:^30} | {1:^22} | {2:^50} | {3:^12} | {4:^12} |'.format('Alias', 'ContractName', 'Address', 'ABI', 'Bytecode'))
        self.logger.info(' ' + STRING_DASHES)
        for artifact_identifier in self.contract_data:
            # Temporary fix for showing ( True | False ) that the abi & bytecode are present
            if len(self.contract_data[artifact_identifier]['abi']) > 1:
                abi_status = True
            if len(self.contract_data[artifact_identifier]['bytecode']) > 1:
                bytecode_status = True

            self.logger.info('| {0:^30} | {1:^22} | {2:^50} | {3:^12} | {4:^12} |'.format(
                str(artifact_identifier), str(self.contract_data[artifact_identifier]['name']),
                str(self.contract_data[artifact_identifier]['address']), str(abi_status), str(bytecode_status))
            )
        self.logger.info(' ' + STRING_DASHES)

    def new_contract_entry(self, contract_name, contract_instance, contract_abi, contract_bytecode, contract_address):
        """ New Contract Entry
        This function will generate a new entry dictionary for a contract_cli artifact that has been loaded
        :param contract_name:
        :param contract_instance:
        :param contract_abi:
        :param contract_bytecode:
        :param contract_address:
        :return:  New dict with name, instance, abi, bytecode and address
        """
        return {
            'name': contract_name, 'instance': contract_instance, 'abi': contract_abi,
            'bytecode': contract_bytecode, 'address': contract_address
        }

    def add_contract_artifact(self, contract_name, contract_instance, contract_abi, contract_bytecode, contract_address, alias=''):
        """ Add Artifacts
        This function will add a new entry to the contract_data
        :param contract_name:
        :param contract_instance:
        :param contract_abi:
        :param contract_bytecode:
        :param contract_address:
        :param alias:
        :return:
        """
        if alias != '':
            self.contract_data[str(alias)] = self.new_contract_entry(
                contract_name, contract_instance, contract_abi, contract_bytecode, contract_address
            )
        else:
            self.contract_data[str(contract_name)] = self.new_contract_entry(
                contract_name, contract_instance, contract_abi, contract_bytecode, contract_address
            )