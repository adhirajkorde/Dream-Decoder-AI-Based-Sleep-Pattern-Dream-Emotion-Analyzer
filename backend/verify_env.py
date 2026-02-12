import sys
import os

def verify():
    print("=" * 50)
    print("Dream Decoder - Environment Verification")
    print("=" * 50)
    
    # Check Python version
    print(f"Python version: {sys.version}")
    
    # Check dependencies
    dependencies = [
        ('flask', 'flask'),
        ('flask_cors', 'flask-cors'),
        ('transformers', 'transformers'),
        ('torch', 'torch'),
        ('spacy', 'spacy'),
        ('dateutil', 'python-dateutil'),
        ('fpdf', 'fpdf2')
    ]
    
    missing = []
    for module_name, package_name in dependencies:
        try:
            module = __import__(module_name)
            version = getattr(module, '__version__', 'unknown')
            print(f"✅ {package_name} is installed (version: {version})")
        except ImportError:
            print(f"❌ {package_name} is NOT installed")
            missing.append(package_name)
            
    # Check SpaCy model
    if 'spacy' not in missing:
        import spacy
        try:
            spacy.load('en_core_web_sm')
            print("✅ SpaCy model 'en_core_web_sm' is available")
        except:
            print("❌ SpaCy model 'en_core_web_sm' is NOT available")
            missing.append('spacy-model')
            
    # Check Transformers pipeline (lazy load check)
    if 'transformers' not in missing and 'torch' not in missing:
        try:
            from transformers import pipeline
            print("✅ Transformers pipeline is working")
        except Exception as e:
            print(f"❌ Transformers pipeline failed: {e}")
            missing.append('transformers-pipeline')

    print("=" * 50)
    if not missing:
        print("ALL SYSTEMS GO! Environment is healthy.")
        return True
    else:
        print(f"FAILED: Missing or broken components: {', '.join(missing)}")
        print("Please run 'setup.bat' again.")
        return False

if __name__ == "__main__":
    success = verify()
    sys.exit(0 if success else 1)
