# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/parser.ipynb.

# %% auto 0
__all__ = ['TreeSitterParser']

# %% ../nbs/parser.ipynb 2
import CodeSyntaxConcept

from .tokenizer import CodeTokenizer, get_token_type
import CodeSyntaxConcept.utils as utils
import pandas as pd

# %% ../nbs/parser.ipynb 4
class TreeSitterParser:
    
    def __init__(self, tokenizer: CodeTokenizer):
        self.tokenizer = tokenizer

    def process_source_code(self,source_code: str):
        ast_representation = self.tokenizer.parser.parse(bytes(source_code, "utf8"))
        ast_nodes = []
        utils.traverse(ast_representation.root_node, ast_nodes)
        source_code_ast_types = []
        for node_index, node in enumerate(ast_nodes):
            #source_code_ast_types.append([node.text.decode("utf-8"), self.tokenizer.node_types.index(node.type), self.tokenizer.node_types.index(node.parent.type)])
            source_code_ast_types.append((node.text.decode("utf-8"), node.type, node.parent.type))
        return pd.DataFrame(source_code_ast_types, columns=['input', 'ast_concept', 'parent_ast_concept'])

    def process_model_source_code(self, source_code: str):
        source_code_encoding = self.tokenizer(source_code)
        source_code_ast_types = []
        for input_id_index, input_id in enumerate(source_code_encoding['input_ids']):
            #source_code_ast_types.append([input_id, source_code_encoding['ast_ids'][input_id_index], source_code_encoding['parent_ast_ids'][input_id_index]])
            source_code_ast_types.append((
                input_id, 
                'ERROR' if source_code_encoding['ast_ids'][input_id_index] == -1 else self.tokenizer.node_types[source_code_encoding['ast_ids'][input_id_index]], 
                'ERROR' if source_code_encoding['ast_ids'][input_id_index] == -1 else self.tokenizer.node_types[source_code_encoding['parent_ast_ids'][input_id_index]]))
        return source_code_encoding, pd.DataFrame(source_code_ast_types, columns=['input_id', 'ast_concept', 'parent_ast_concept'])
