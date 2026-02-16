#!/bin/bash
# Script de Preparação para GitHub Push
# Execute este script para verificar tudo antes de fazer push

echo "🔍 Verificando Backend_Control_System para GitHub..."
echo ""

# 1. Verificar Python syntax
echo "1️⃣  Verificando sintaxe Python..."
python3 -m py_compile app/main.py app/config.py 2>&1
if [ $? -eq 0 ]; then
    echo "   ✅ Sintaxe Python OK"
else
    echo "   ❌ Erro de sintaxe Python!"
    exit 1
fi
echo ""

# 2. Verificar arquivos importantes
echo "2️⃣  Verificando arquivos importantes..."
files=(
    "app/main.py"
    "app/config.py"
    "requirements.txt"
    ".env.example"
    "Dockerfile"
    "docker-compose.yml"
    "README.md"
    "DEPLOYMENT.md"
)

for file in "${files[@]}"; do
    if [ -f "$file" ]; then
        echo "   ✅ $file"
    else
        echo "   ❌ $file NÃO ENCONTRADO!"
        exit 1
    fi
done
echo ""

# 3. Verificar .env não será commitado
echo "3️⃣  Verificando proteção de .env..."
if grep -q "^.env$" .gitignore && grep -q "^\*.env" .gitignore; then
    echo "   ✅ .env protegido no .gitignore"
else
    echo "   ⚠️  Verificar .gitignore manualmente"
fi
echo ""

# 4. Listar documentação
echo "4️⃣  Documentação disponível:"
ls -1 *.md | while read file; do
    size=$(wc -c < "$file" | numfmt --to=iec 2>/dev/null || wc -c < "$file")
    echo "   ✅ $file ($size)"
done
echo ""

# 5. Git status
echo "5️⃣  Git status:"
git status --short | head -20
echo ""

echo "✨ Checklist pré-push:"
echo ""
echo "[ ] Leu GITHUB_CHECKLIST.md"
echo "[ ] Testou localmente: uvicorn app.main:app --reload"
echo "[ ] Verificou endpoints em http://localhost:8000/docs"
echo "[ ] Confirmou DATABASE_URL no .env"
echo "[ ] Revisou README.md"
echo ""

echo "🚀 Pronto para fazer push?"
echo ""
echo "Próximos comandos:"
echo "  git add ."
echo "  git commit -m 'chore: Production-ready backend v2.0.0'"
echo "  git push origin main"
echo ""

echo "✅ Verificação concluída!"
