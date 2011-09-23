# This is used by GYP to generate platform-specific project files for building
# Finch. (I.e. on a Mac it will create an XCode project, on Linux a makefile.)
# See README for more.

{
  'targets': [
    {
      'target_name': 'finch',
      'type': 'executable',
      'include_dirs': [
        'src/Base',
        'src/Compiler',
        'src/Interpreter',
        'src/Test',
      ],
      'sources': [
        'src/Base/Array.h',
        'src/Base/Dictionary.h',
        'src/Base/FinchString.cpp',
        'src/Base/FinchString.h',
        'src/Base/Macros.h',
        'src/Base/Queue.h',
        'src/Base/Ref.h',
        'src/Base/Stack.h',
        'src/Base/StringTable.cpp',
        'src/Base/StringTable.h',
        'src/Compiler/BlockTable.cpp',
        'src/Compiler/BlockTable.h',
        'src/Compiler/CodeBlock.cpp',
        'src/Compiler/CodeBlock.h',
        'src/Compiler/Compiler.cpp',
        'src/Compiler/Compiler.h',
        'src/finch.1',
        'src/IErrorReporter.h',
        'src/IInterpreterHost.h',
        'src/Interpreter/Environment.cpp',
        'src/Interpreter/Environment.h',
        'src/Interpreter/Fiber.cpp',
        'src/Interpreter/Fiber.h',
        'src/Interpreter/FileLineReader.cpp',
        'src/Interpreter/FileLineReader.h',
        'src/Interpreter/Objects/ArrayObject.h',
        'src/Interpreter/Objects/BlockObject.h',
        'src/Interpreter/Objects/DynamicObject.cpp',
        'src/Interpreter/Objects/DynamicObject.h',
        'src/Interpreter/Objects/FiberObject.h',
        'src/Interpreter/Objects/NumberObject.h',
        'src/Interpreter/Objects/Object.cpp',
        'src/Interpreter/Objects/Object.h',
        'src/Interpreter/Objects/StringObject.h',
        'src/Interpreter/Primitives/ArrayPrimitives.cpp',
        'src/Interpreter/Primitives/ArrayPrimitives.h',
        'src/Interpreter/Primitives/BlockPrimitives.cpp',
        'src/Interpreter/Primitives/BlockPrimitives.h',
        'src/Interpreter/Primitives/FiberPrimitives.cpp',
        'src/Interpreter/Primitives/FiberPrimitives.h',
        'src/Interpreter/Primitives/NumberPrimitives.cpp',
        'src/Interpreter/Primitives/NumberPrimitives.h',
        'src/Interpreter/Primitives/ObjectPrimitives.cpp',
        'src/Interpreter/Primitives/ObjectPrimitives.h',
        'src/Interpreter/Primitives/StringPrimitives.cpp',
        'src/Interpreter/Primitives/StringPrimitives.h',
        'src/Interpreter/Primitives.cpp',
        'src/Interpreter/Primitives.h',
        'src/Interpreter/Scope.cpp',
        'src/Interpreter/Scope.h',
        'src/Interpreter.cpp',
        'src/Interpreter.h',
        'src/main.cpp',
        'src/ReplLineReader.cpp',
        'src/ReplLineReader.h',
        'src/StandaloneInterpreterHost.cpp',
        'src/StandaloneInterpreterHost.h',
        'src/Syntax/AST/ArrayExpr.h',
        'src/Syntax/AST/BindExpr.h',
        'src/Syntax/AST/BlockExpr.h',
        'src/Syntax/AST/DefineExpr.h',
        'src/Syntax/AST/Expr.cpp',
        'src/Syntax/AST/Expr.h',
        'src/Syntax/AST/IExprVisitor.h',
        'src/Syntax/AST/MessageExpr.h',
        'src/Syntax/AST/NameExpr.h',
        'src/Syntax/AST/NumberExpr.h',
        'src/Syntax/AST/ObjectExpr.h',
        'src/Syntax/AST/SelfExpr.h',
        'src/Syntax/AST/SequenceExpr.h',
        'src/Syntax/AST/SetExpr.h',
        'src/Syntax/AST/StringExpr.h',
        'src/Syntax/AST/UndefineExpr.h',
        'src/Syntax/AST/VarExpr.h',
        'src/Syntax/FinchParser.cpp',
        'src/Syntax/FinchParser.h',
        'src/Syntax/ILineReader.h',
        'src/Syntax/ITokenSource.h',
        'src/Syntax/Lexer.cpp',
        'src/Syntax/Lexer.h',
        'src/Syntax/LineNormalizer.cpp',
        'src/Syntax/LineNormalizer.h',
        'src/Syntax/Parser.cpp',
        'src/Syntax/Parser.h',
        'src/Syntax/Token.cpp',
        'src/Syntax/Token.h',
        'src/Test/ArrayTests.cpp',
        'src/Test/ArrayTests.h',
        'src/Test/LexerTests.cpp',
        'src/Test/LexerTests.h',
        'src/Test/QueueTests.cpp',
        'src/Test/QueueTests.h',
        'src/Test/RefTests.cpp',
        'src/Test/RefTests.h',
        'src/Test/StackTests.cpp',
        'src/Test/StackTests.h',
        'src/Test/StringTests.cpp',
        'src/Test/StringTests.h',
        'src/Test/Test.cpp',
        'src/Test/Test.h',
        'src/Test/TestMain.cpp',
        'src/Test/TestMain.h',
        'src/Test/TokenTests.cpp',
        'src/Test/TokenTests.h'
      ],
    },
  ],
}